// ECE 4012 Resistive NN Emulator Team
// This .cpp file provides helper functions for common neural network operations


// This function performs 2d convolution on inputs for given filter matrices
// >>> Intro to conv layers: http://machinelearninguru.com/computer_vision/basics/convolution/convolution_layer.html <<<
//
// @params:
//  input: a pointer to the memory start location containing the input matrix (1D, index with y * width + x)
//  output: a pointer to a chunk of allocated memory for output matrix (1D)
//  filter: a pointer to the memory start location containing the filter matrix (1D)
//  input_size: specifies the length of one input side (assuming square input shape)
//  num_input_channels: specifies number of input channels (so that the total input size is input_size * input_size * num_input_channels)
//  filter_size: specifies the length of one filter side (assuming square filter shape)
//  num_output_channels: specifies number of output channels
//  padding: whether the input should be padded to avoid shrink of size after convolution
void conv2d(float* input, float* output, float* filter, int input_size, int num_input_channels, int filter_size, int num_output_channels, bool padding=true) {



}







// This function adds bias to the input
//
// @params:
//  input: a pointer to the memory start location containing the input matrix (1D, index with y * width + x)
//  output: a pointer to a chunk of allocated memory for output matrix (1D)
//  bias: a pointer to the memory start location containing the filter matrix (1D)
//  input_legnth: specifies the overall length of the input (and the bias has the same length)
void add_bias(float* input, float* output, float* bias, int input_length) {
    for (int i = 0; i < input_legnth; i++) {
        output[i] = bias[i] + input[i];
    }
}







// This function performs 2d max pooling for the given input
//
// @params:
//  input: a pointer to the memory start location containing the input matrix (1D, index with y * width + x)
//  output: a pointer to a chunk of allocated memory for output matrix (1D)
//  input_side_length: specifies the length of one input side (assuming square input shape & divisible by 2)
//  num_input_channels: specifies number of input channels (so that the total input size is input_side_length * input_side_length * num_input_channels)
//  pool_size: how large the pool are should be (pooling over an area of size pool_size * pool_size)
void max_pool_2d(float* input, float* output, int input_side_length, int num_input_channels, int pool_size) {



}







// This function performs ReLU activation
//
// @params:
//  input: a pointer to the memory start location containing the input matrix (1D, index with y * width + x)
//  output: a pointer to a chunk of allocated memory for output matrix (1D)
//  input_side_length: specifies the length of one input side (assuming square input shape & divisible by 2)
//  num_input_channels: specifies number of input channels (so that the total input size is input_side_length * input_side_length * num_input_channels)
void relu(float* input, float* output, int input_side_length, int num_input_channels) {



}





// This function performs matrix multiplication for fully connected layers
// It multiplies a matrix of size (l * w) with a vector of size w.
// see this ---> https://drive.google.com/file/d/1oSvZW24r5zVvIbOgpraziA48do0RH-_f/view?usp=sharing
//
// @params:
//  matrix: a pointer to the memory start location containing the input matrix (1D, index with y * width + x)
//  vector: a pointer to the memory start location containing the input vector (its length is matrix_w)
//  output: a pointer to a chunk of allocated memory for output matrix (1D)
//  matrix_l & matrix_w: specifies the size of the matrix
void mat_mul(float* matrix, float* output, int matrix_l, int matrix_w) {



}
