version 1.00:
1 Convolutional layer with 32 filters (3x3) kernel
MaxPooling with (2x2)
Flatten
Hidden layer with 128 units + Droupout(0.5)
- Training Accuracy: 31.00% -> 84.93%
- Training Loss: 2.5875 -> 0.2204
- Validation Accuracy (last epoch): 95.37%
- Test Accuracy: 95.60%
- Test Loss: 0.1940

version 1.50:
2 Convolutional layers with 32 filters, (3x3) kernel
MaxPooling with (2x2) after each convolutional layer
Flatten
Dense layer with 128 units + Droupout(0.5)
- Training Accuracy: 32.13% -> 94.65%
- Validation Accuracy: 68.25% -> 97.62%
- Test Accuracy: 97.44%
- Loss:
    - Training: 2.4895 -> 0.1675
    - Validation: 1.1970** -> 0.0896
    - Test: 0.0911

version 1.51:
2 Convolutional layers with 32 filters and 64 filters respectively, (3x3) kernel
MaxPooling with (2, 2) after each convolutional layer
Flatten
Dense layer with 128 units + Droupout(0.5)
- Training Accuracy: 31.07% -> 93.94%
- Validation Accuracy: 61.65% -> 98.40%
- Test Accuracy: 98.14%
- Loss:
    - Training: 2.5379 -> 0.1906
    - Validation: 1.4082 -> 0.0788
    - Test: 0.0770

version 1.512:
2 convolutional layers both with 64 filters, (3x3) kernel
MaxPooling with (2x2) after each convolutional layer
Flatten
Dense layer with 128 units + Droupout(0.5)
- Training Accuracy: 29.62% -> 92.27%
- Validation Accuracy: 66.12% -> 97.90%
- Test Accuracy: 98.25%
- Loss:
    - Training: 2.6265 -> 0.2331
    - Validation: 1.3581 -> 0.0873
    - Test: 0.0747

Conclusion: Adding additional convolutional layers and Dense layers with filters are usefull unless it starts overfitting.
