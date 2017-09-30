# -*- coding: utf-8 -*-
# @Author: 541435721
# @Date:   2017-09-30 10:53:37
# @Last Modified by:   541435721
# @Last Modified time: 2017-09-30 10:57:55


import os
import SimpleITK as sitk

names = os.listdir('./')

for x in names:
    img = sitk.ReadImage(x)
    img.SetSpacing([0.57, 0.57, 1.6])
    sitk.WriteImage(img, 'spacing' + x)
