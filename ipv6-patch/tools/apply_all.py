# -*- coding: utf-8 -*-
"""一键复现：从上游 v7.0.1 release 附件生成打好 IPv6 补丁的 bundle。

用法：
    python tools/apply_all.py <官方 v7.0.1 的 room-elves-card.js> <输出目录>

例如：
    python tools/apply_all.py ./room-elves-card.js ./dist

流程：
  1. 校验输入确为 v7.0.1 基线（含上游内置的 iKuai 4.0 信封分支、不含 IPv6 方法）；
  2. 依次应用 4 个最小补丁（每个都会校验锚点唯一，任一不符即报错退出）；
  3. 重新生成 .js.gz（gzip level 9、无时间戳，可复现）；
  4. 输出并打印 SHA-256。

注意：本脚本只做纯文本替换，不联网、不读取任何配置、不含任何实机信息。
"""
import io, os, sys, shutil, subprocess, tempfile, gzip, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
STEPS = [
    '1_ipv6_clients.py',       # IPv6 终端分组列出
    '2_units_connections.py',  # 单位换算 + 连接详情查询
    '3_recalibrate.py',        # 按爱快 4.0 实机抓包校准载荷
    '4_display_fix.py',        # 长值不截断 + 字段中文标签
]


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    src, outdir = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2])
    if not os.path.isfile(src):
        print('输入文件不存在:', src)
        return 2
    base = io.open(src, encoding='utf-8', errors='replace').read()
    if 'void 0===i.Result&&"number"==typeof i.code' not in base:
        print('错误：输入不含 v7.0.1 内置的 iKuai 4.0 信封分支，请确认是官方 v7.0.1 release 附件。')
        return 1
    if '_ikuaiAllV6Entity' in base:
        print('错误：输入已包含 IPv6 补丁，请勿重复应用。')
        return 1

    work = tempfile.mkdtemp(prefix='room-elves-v7-')
    try:
        target = os.path.join(work, 'room-elves-card.js')
        shutil.copyfile(src, target)
        for step in STEPS:
            script = os.path.join(HERE, step)
            print('==>', step)
            r = subprocess.run([sys.executable, script], cwd=work,
                               capture_output=True, text=True,
                               encoding='utf-8', errors='replace')
            print(r.stdout.rstrip())
            if r.returncode:
                print(r.stderr.rstrip())
                print('补丁失败:', step)
                return 1

        js = io.open(target, 'rb').read()
        # 语法校验（若本机有 node）
        try:
            chk = subprocess.run(['node', '--check', target],
                                 capture_output=True, text=True)
            if chk.returncode:
                print('node --check 失败:', chk.stderr[:400])
                return 1
            print('node --check: PASS')
        except FileNotFoundError:
            print('node 未安装，跳过语法校验')

        buf = io.BytesIO()
        with gzip.GzipFile(filename='', mode='wb', fileobj=buf,
                           compresslevel=9, mtime=0) as f:
            f.write(js)
        gz = buf.getvalue()
        assert gzip.decompress(gz) == js, 'gz 回读不一致'

        os.makedirs(outdir, exist_ok=True)
        io.open(os.path.join(outdir, 'room-elves-card.js'), 'wb').write(js)
        io.open(os.path.join(outdir, 'room-elves-card.js.gz'), 'wb').write(gz)
        print()
        print('输出:', outdir)
        print('  room-elves-card.js     %d B  sha256 %s' %
              (len(js), hashlib.sha256(js).hexdigest()))
        print('  room-elves-card.js.gz  %d B  sha256 %s' %
              (len(gz), hashlib.sha256(gz).hexdigest()))
        print('DONE')
        return 0
    finally:
        shutil.rmtree(work, ignore_errors=True)


if __name__ == '__main__':
    sys.exit(main())
