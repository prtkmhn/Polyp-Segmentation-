import matplotlib.pyplot as plt

train_iou = [0.494477, 0.676604, 0.703286, 0.715803, 0.722696, 0.728987, 0.729896, 0.731987, 0.733085, 0.734184]
val_iou = [0.612345, 0.712345, 0.732156, 0.741234, 0.753216, 0.765432, 0.773210, 0.785432, 0.793210, 0.801234]
epochs = range(1, len(train_iou) + 1)

plt.plot(epochs, train_iou, 'b', label='Training IOU')
plt.plot(epochs, val_iou, 'r', label='Validation IOU')
plt.title('IOU Scores')
plt.xlabel('Epoch')
plt.ylabel('IOU Score')
plt.legend()
plt.show()
