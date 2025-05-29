Configuration Guide
This file explains the settings in config.json for running the local LLM.

What each setting means
model_path
The location of your model file on your computer. For example, "models/my-model.gguf". Make sure the path matches where you actually put the model.

context_length
How much text the model keeps in memory while running. Bigger values let the model remember more but use more RAM.
Usually, 4096 works well.

gpu_layers
How many layers of the model you want to run on your GPU. Running more on GPU can make things faster if you have a compatible graphics card. Adjust this depending on your GPU’s memory.

threads
Number of CPU threads to use for running the model. More threads can speed things up but might slow down other programs.
8 is a common starting point.

Tips
If you don’t have a GPU that supports CUDA, set gpu_layers to 0 so everything runs on CPU.

Double-check the model_path points to where your model actually is.

Feel free to tweak these values to get the best performance for your system.
