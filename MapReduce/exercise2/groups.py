#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys


culo = ['culo', 'nalgas', 'trasero']
polla = ['nabo', 'polla', 'pene', 'pija', 'pilila']
tetas = ['pechos', 'tetas', 'melones']
chocho  = ['coño', 'chocho', 'vagina','concha', 'chochete']

cculo = 0
cpolla = 0
ctetas  = 0
cchocho = 0

previous_key = None
total = 0


def output(previous_key, total):
    print previous_key + " \t " + str(total)

for line in  sys.stdin:
    if '\t' in line:
        key, value = line.split("\t", 1)
        if key in culo:
            cculo += 1
        if key in polla:
            cpolla += 1
        if key in tetas:
            ctetas += 1
        if key in chocho:
            cchocho += 1

print 'Chochos: ' + str(cchocho)
print 'Pollas: ' + str(cpolla)
print 'Culos: ' + str(cculo)
print 'Tetas: ' + str(ctetas)

