// This function performs 2d max pooling for the given input
//
// @params:
//  input: a pointer to the memory start location containing the input matrix (1D, index with y * width + x)
//  output: a pointer to a chunk of allocated memory for output matrix (1D)
//  input_side_length: specifies the length of one input side (assuming square input shape & divisible by 2)
//  num_input_channels: specifies number of input channels (so that the total input size is input_side_length * input_side_length * num_input_channels)
//  pool_size: how large the pool are should be (pooling over an area of size pool_size * pool_size)
void max_pool_2d(float* input, float* output, int input_side_length, int num_input_channels, int pool_size) {
    int i, j, k, m, n;
    float max = -99999;
    int chunk = input_side_length / pool_size;
    int count = 0;

    for (i = 0; i < num_input_channels; i++) {
	for (j = 0; j < chunk; j++) {
	    for (k = 0; k < chunk; k++) {
		for (m = 0; m < pool_size; m++) {
		    for (n = 0; n < pool_size; n++) {
			float temp = input[i * input_side_length * input_side_length + j * chunk * pool_size * pool_size + k * pool_size + input_side_length * m + n];		
			if (temp > max) {
			    max = temp;
			}
		    }
		}
		output[count] = max;
		max = -99999;
		count = count + 1;
	    }	
	}
    }
}
