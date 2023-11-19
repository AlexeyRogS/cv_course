# Week 4 (Classification and object detection)

This week is dedicated to object recognition tasks (in particular we will be looking into object detection task as the most interesting in practice). You will learn
how object detection models work and how to use them. That is how to train and
inference object detection models.

* A follow-up seminar on image classification. We review how optimization works and
how to use torch optimizers and build our first CNN for cifar classification (optim_cifar.ipynb)
* [Lecture slides](https://docs.google.com/presentation/d/1-B0z3TWHLZmCHbcK4nEjTLkz5Ka3m8-P98yPwXshFso/edit#slide=id.g295ea1ffee4_0_134)
* Seminar on object detection. We discuss in detail how to compute IoU and mAP and
study the code for mAP. Then we look in more detail at how augmentations work and
used torch transformations as well as albumentations. We review object detection
models and train Mask R-CNN for pedestrian detection. (object_detection.ipynb)
* TrickingCNN.ipynb contains a funny example of how we can manipulate a trained model into making mistakes.
