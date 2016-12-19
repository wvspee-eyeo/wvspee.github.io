import os
import json

def foo():
    path = 'chrome/locale'
    out_files = {}
    for locale in os.listdir(path):
        if not locale:
            continue

        file_ = '{}/{}/global.properties'.format(path, locale)
        out_file = '../adblockplusui/locale/{}/antiadblockInit.json'.format(locale)

        if not os.path.exists(file_):
            continue

        lines = []
        with open(file_) as f:
            for line in f.readlines():
                if line.startswith('notification_antiadblock_'):
                    id_, msg = line.replace('\n', '').split('=')
                    out_files.setdefault(out_file, {})[id_] = {'message': msg}
                else:
                    lines.append(line)

        with open(file_, 'w+') as f:
            for l in lines:
                f.write(l)

    for out_file, msgs in out_files.items():
        if not os.path.exists(os.path.dirname(out_file)):
            os.mkdir(os.path.dirname(out_file))
        with open(out_file, 'wb') as f:
            for l in json.dumps(msgs, indent=2).split('\n'):
                f.write('%s\n' % l.rstrip())


if __name__ == '__main__':
    foo()
