import subprocess
cp = subprocess.run(
    [
      'curl',
      'https://www.jma.go.jp/jma/index.html'
    ],
    stdout=subprocess.PIPE
)

if cp:
    print(cp)
else:
    print('faild')
