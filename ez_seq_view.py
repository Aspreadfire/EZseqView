# coding:utf-8
# import docker
import os
import subprocess as sp
import pandas as pd

# client = docker.from_env()
# container = client.containers.run(
#     image='trinityrnaseq/trinityrnaseq:2.14.0',
#     command=['/usr/local/bin/Trinity', '-h'], 废弃方案，无法调用容器内commend
#     remove=True,
#     volumes={os.getcwd(): {'bind': '/data/input', 'mode': 'rw'}}
# )

cpu_used = int(len(os.sched_getaffinity(0)) / 2)
if cpu_used < 1:
    cpu_used = 1
else:
    cpu_used = int(len(os.sched_getaffinity(0)) / 2)

sp.call('podman run --rm -v $(pwd):$(pwd) --privileged=true trinityrnaseq/trinityrnaseq:2.14.0 Trinity',
        shell=True)

sp.call(f'podman run --rm -v {os.getcwd()}:/data/input --privileged=true localhost/r_package:1.0 ls -l', shell=True)


def run_hisat2(sample):
    for line in sample:
        sp.call(f'docker run --rm -v {os.getcwd()}:/data/input --privileged=true docker.io/aspreadfire/hisat2:2.2.1 '
                f'hisat2 -p {cpu_used} --dta -x 84K_genome/84K_genome '
                f'-1 {line}.fq '
                f'-2 {line}.fq '
                f'-S hisat2_result/{line}.sam',
                shell=True)


def run_hisat2_sort(sample):
    for line in sample:
        sp.call(f'docker run --rm -v {os.getcwd()}:/data/input --privileged=true docker.io/aspreadfire/hisat2:2.2.1 '
                f'samtools sort -@ {cpu_used}'
                f'-o sam_result/{line}.bam hisat2_result/{line}.sam',
                shell=True)


def run_stringtie(sample):
    for line in sample:
        sp.call(f'docker run --rm -v {os.getcwd()}:/data/input --privileged=true localhost/stringtie:2.2.1 '
                f'samtools sort -@ {cpu_used}'
                f'-o sam_result/{line}.bam hisat2_result/{line}.sam',
                shell=True)


def run_ballgown(sample):
    for line in sample:
        sp.call(f'docker run --rm -v {os.getcwd()}:/data/input --privileged=true localhost/stringtie:2.2.1 '
                f'samtools sort -@ {cpu_used}'
                f'-o sam_result/{line}.bam hisat2_result/{line}.sam',
                shell=True)


if __name__ == '__main__':
    run_stringtie()
