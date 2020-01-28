import os
import platform
import subprocess

import click


@click.group()
def cli():
    pass


@click.command()
def install_zsh():
    # mac
    if platform.platform().startswith('Darwin'):
        subprocess.call(['brew', 'install ', 'zsh'], shell=True)
    else:
        subprocess.call(['sudo', ' apt-get', 'update', '&&' 'install', '-y', 'zsh'])


@click.command()
def setup_hexo():
    os.system('sudo apt-get update && apt-get install -y nodejs nginx git')
    os.system('node -v')
    os.system('adduser git')
    os.system('chmod 740 /etc/sudoers')
    os.system('echo  git ALL=(ALL) ALL >> /etc/sudoers')
    os.system('chmod 400 /etc/sudoers ')
    os.system('echo jianpan |sudo passwd git --stdin')
    os.system('su git')
    os.system('mkdir .ssh && chmod 700 .ssh')
    os.system('touch .ssh/authorized_keys && chmod 600 .ssh/authorized_keys')
    os.system('mkdir /var/repo &&cd /var/repo && git init --bare blog.git')
    os.system(
        'echo #!/bin/sh \n git --work-tree=/var/www/hexo --git-dir=/var/repo/blog.git checkout -f >>  /var/repo/blog.git/hooks/post-receive')
    os.system('chmod +x /var/repo/blog.git/hooks/post-receive')
    os.system('chown -R git:git blog.git')


@click.command()
def dropdb():
    click.echo('Dropped the database')


cli.add_command(setup_hexo)
cli.add_command(dropdb)

if __name__ == '__main__':
    cli()
