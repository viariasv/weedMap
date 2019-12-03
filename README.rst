.. raw:: html

    <p align="center">
      <img width="400" height="200" src="https://github.com/viariasv/weedMap/blob/master/images/logo.jpg">
    </p>

    <h1 align="center"><b>weedMap</b>: A Large-Scale Semantic Weed Mapping Framework Using Aerial Multispectral Imaging and Deep Neural Network for Precision Farming</h1>

This repository contains the implementation of this `paper <https://www.mdpi.com/2072-4292/10/9/1423/htm>`__. A convolutional neural network used to crop/weed semantic segmentation  in  multispectral images obtained from an unmanned aerial vehicle (UAV). This is a multiclass classification task: the neural network predicts if each pixel in the multiespectral image is either a crop, weed or background. The neural network structure is derived from the *SegNet* architecture, described in this `paper <https://arxiv.org/pdf/1511.00561.pdf>`__. 

Table of Contents
~~~~~~~~~~~~~~~~~
 - `Database`_
 - `Experimental Setup`_
 - `Create a virtual environment`_
 - `Requirements`_
 - `Results`_
 - `Change log`_
 - `Citing`_
 - `License`_

Database
~~~~~~~~

.. raw:: html

    <p align="justify">
    The following information details the sugar beet and weed datasets, including file naming conventions, sensor specifications, and tiled and orthomosaic data.
    </p>
    <p align="justify">
    The picture below exemplifies one of the datasets used in this study. The left image shows the entire orthomosaic map, and the middle and right are subsets of each area at varying zoom levels. The yellow, red, and cyan boxes indicate different areas on the field, corresponding to cropped views. These details clearly evidence the large scale of the farm field and suggest the visual challenges in distinguishing between crops and weeds (limited number of pixels and similarities in appearance).
    </p>
    <p align="center">  
      <img width="300" height="100" src="https://github.com/viariasv/weedMap/blob/master/images/orthomosaic_1.jpg">
    </p>

    <p align="justify">
    The figure below shows an example UAV trajectory covering a 1,300 square meter sugar beet field. Each yellow frustum indicates the position where an image was taken, and the green lines are rays between a 3D point and their co-visible multiple views. Qualitatively, it can be seen that the 2D feature points from the right subplots are properly extracted and matched for generating a precise orthomosaic map. A similar coverage-type flight path is used for our dataset acquisitions.
    </p>
    <p align="center">
      <img width="250" height="250" src="https://github.com/viariasv/weedMap/blob/master/images/orthomosaic_2.jpg">
    </p>

.. raw:: html

    <h2 align="justify">Multispectral camera specifications
    </h2>
    <p align="justify">
    
    The table below elaborates the multispectral sensor specifications. More detailed product information can be found on the Micasense webpage (<a href="https://www.micasense.com/rededge-m">RedEdge-M</a>  and <a href="https://www.parrot.com/business-solutions-us/parrot-professional/parrot-sequoia">Sequoia</a>).
    </p>

    <p align="center">  
      <img width="300" height="200" src="https://github.com/viariasv/weedMap/blob/master/images/specifications_1.png">
    </p>

    <p align "justify">
    The two data collection campaigns cover a total area of 16,554 square meters as shown in the table below. The two cameras we used can capture 5 and 4 raw image channels, and we compose them to obtain RGB and CIR images by stacking the R, G, B channels for an RGB image (RedEdge-M) and R, G, and NIR for a CIR image (Sequoia). We also extract the Normalized Difference Vegetation Index (NDVI). These processes result in 12 and 8 channels for the RedEdge-M and Sequoia camera, respectively. We treat each channel as an image, resulting in a total of 1.76 billion pixels composed of 1.39 billion training pixels and 367 million testing pixels (10,196 images). To our best knowledge, this is the largest publicly available dataset for a sugar beet field containing multispectral images and their pixel-level ground truth.
    </p>
