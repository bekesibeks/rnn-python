import numpy as np

Wxh = np.random.randn(2, 2) * 0.01  # input to hidden
Why = np.random.randn(2, 1) * 0.01  # hidden to output
bh = [0,0]  # hidden bias
by = [0]  # output bias

training_samples = [[0,1],[1,1],[1,0],[0,0]]
training_sample_solutions = [1,0,1,0]


output_hidden = []

def feed_input(input, target):
    sum_of_inputs_h = np.dot(Wxh, input);
    added_bias_h = sum_of_inputs_h + bh;

    output_hidden = np.tanh(added_bias_h)

    sum_of_inputs_y = np.dot(output_hidden, Why)
    added_bias_y = sum_of_inputs_y + by;

    output_y = np.tanh(added_bias_y)

    loss = output_y - target
    return loss, output


for a,b in zip(training_samples, training_sample_solutions):
    loss, output = feed_input(a,b)
    print(a,b)
    print("- output and loss: ")
    print(output, loss)