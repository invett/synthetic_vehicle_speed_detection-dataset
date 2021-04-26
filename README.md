<div align="center">    
 
# A Synthetic Dataset for Vehicle Speed Detection      
[![Paper](http://img.shields.io/badge/paper-arxiv.2104.09903-B31B1B.svg)](https://arxiv.org/abs/2104.09903)

</div>

---

## Introduction

---

This is a synthetic dataset built to develop an intelligent speed detection system. This dataset has been generated with the Carla Simulator, and has sequences recorded from a single point of view, with a camera centered on the road at a height of 3 meters, with an inclination of 45 degrees.

"Data-driven vehicle speed detection from synthetic driving simulator images", A. Hernández, et. al., 2021 [[arxiv](https://arxiv.org/abs/2104.09903)]

<p align="center">
  <img src="figs/Image01.jpg" width="280" />
  <img src="figs/Image02.jpg" width="280" /> 
  <img src="figs/Image03.jpg" width="280" />
</p>

You can download the dataset (images in JPG format and annotations in JSON-like format) from [here](https://universidaddealcala-my.sharepoint.com/:f:/g/personal/antonio_hernandezm_uah_es/Ekc3fwPznEpBlXMMLf4X6LUBSla5SYtRefCCPG9SPCbxzg?e=GaZTUT)

---

## Requirements

* python                    3.8.5
* numpy                     1.17.4
* pygame                    2.0.0
* Carla                     0.9.10

---

## Citation
Please cite the paper in your publications if it helps your research: 
```
@misc{martinez2021datadriven,
      title={Data-driven vehicle speed detection from synthetic driving simulator images}, 
      author={Antonio Hernández Martínez and Javier Lorenzo Díaz and Iván García Daza and David Fernández Llorca},
      year={2021},
      eprint={2104.09903},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```
