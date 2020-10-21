import mnist_loader
import network

print("gathering data...")
training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
print("data gathered.")
net = network.Network([784, 30, 10])
print("starting to train network")
net.SGD(training_data, 30, 10, 3.0, test_data=test_data)
