<img src='docs/imgs/alien.gif' align="right" width=325>
<br><br><br>

# MeshCNN modification - ML Workshop Home Work


### Team 1 - Oded Carmon, Wisam  Hathot, Yotam Even Nir.


# Cubes (Classification)
### Test accuracy
<img src="/docs/imgs/hw1/cubes_test_acc.png" height="150px"/> 

Logarithmic: 


<img src="/docs/imgs/hw1/cubes_test_acc_logarithmic.png" height="150px"/> 

### Train loss
<img src="/docs/imgs/hw1/cubes_train_loss.png" height="150px"/> 

Logarithmic: 


<img src="/docs/imgs/hw1/cubes_train_loss_logarithmic.png" height="150px"/> 


 ```text
We can see that our modifications to the code have proven to do damage to the high accuracy of the original MeshCNN.
Our choice of parameters, criteria for collapsing edges and other choices we've made, are less optimistic than those
chosen in the original MeshCNN.
But we can see that the accuracy improves during training.
```

### Pooling
The following are plots of pooling results for 4 different configurations:

  - --pool_res 600 444 249 210
 <img src="/docs/imgs/hw1/pool_res_444.png" height="150px"/> 
  - --pool_res 600 450 300 210
 <img src="/docs/imgs/hw1/pool_res_450.png" height="150px"/> 
  - --pool_res 600 483 366 210
 <img src="/docs/imgs/hw1/pool_res_483.png" height="150px"/> 
  - --pool_res 600 561 366 210
 <img src="/docs/imgs/hw1/pool_res_561.png" height="150px"/> 
 
# Human (Segmentation)
### Test accuracy
<img src="/docs/imgs/hw1/cubes_test_acc.png" height="150px"/> 

Logarithmic: 


<img src="/docs/imgs/hw1/cubes_test_acc_logarithmic.png" height="150px"/> 

### Train loss
<img src="/docs/imgs/hw1/cubes_train_loss.png" height="150px"/> 

Logarithmic: 


<img src="/docs/imgs/hw1/cubes_train_loss_logarithmic.png" height="150px"/> 


 ```text
In the case of segmentation we see that our modifications has created major damage to the accuracy and loss.
Not much improvement can be said to have happened during training and the final accuracy results are rather poor.
```

### Visualization
<img src="/docs/imgs/hw1/segmentation.png" height="150px"/>

# Acknowledgments
Our instructor in this course is Rana Hanocka (Tel Aviv University), co-creator of MeshCNN.
