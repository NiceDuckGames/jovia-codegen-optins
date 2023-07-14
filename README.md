# ducky-ai-optins
## Description

This repository provides a platform for Godot 4 users to opt-in their open-source projects for data collection to contribute to the continuous fine-tuning of a Language Model (LM). The collected data will be used to improve the LM's code generation capabilities specifically for Godot 4 projects.

## How to Opt-In

To opt-in your Godot 4 project for data collection, follow these steps:

1. Create an issue on this repository using the "New Issue" button.
2. Use the OPT-IN template for your opt-in issue: (This is the default issue template when you create a new issue)

```
## Opt-In Request: [Your Project Name]

GitHub Repository: [Link to your GitHub repository]
Commit Hash: [Specific commit hash to use]

I would like to opt-in my Godot 4 project for data collection as part of the LM fine-tuning dataset. By opting-in, I acknowledge and agree to the terms and conditions mentioned in the repository's README.md file.

Please find the specific commit hash that represents the version of my project that I want to contribute.

```

1. Fill in the template with the necessary information:
    - Replace `[Your Project Name]` with the name of your project.
    - Provide the `[Link to your GitHub repository]` where your Godot 4 project is hosted.
    - Specify the `[Specific commit hash]` that represents the version of your project you want to contribute.
2. Submit the issue by clicking "Submit new issue".

## Usage

Once you have opted in, we provide a special comment syntax that allows you to control how your code will be used for training. 
You can define additional context for training on a per-script and per-function basis by providing descriptions and example prompts for the training data. 
Below is an example of how to use this syntax in your scripts:

```python
# description: A script containing set of functions that perform simple mathmatical operations
# prompt: Write a simple math library

extends Node

# description: A function that returns the sum of two floats
# prompt: Write an addition function
func add(a: float, b: float) -> float:
	return a + b

# description: A function that returns the difference of two floats
# prompt: Write a subtraction function
func subtract(a: float, b: float) -> float:
	return a - b
```

- `# description:`  a detailed description of the purpose of the function or script.
- `# prompt:`  an example prompt that you would expect this function/script to be the result of.

## Data Privacy and Usage

We prioritize data privacy and respect the rights of contributors. By opting-in your project for data collection, you acknowledge and agree to the following:

- The collected data will be used exclusively for the purpose of fine-tuning a Language Model.
- We will not share your project or its code outside the scope of the LM fine-tuning.
- Your project will be attributed appropriately within the fine-tuning dataset.
- You retain full ownership and control over your project and its associated licenses.

If, at any time, you decide to opt-out or have your project removed from the data collection process, please reach out to us with the necessary details, and we will promptly address your request.

## Licensing

The repository itself is licensed under the [MIT License], and each project contributed is subject to its own respective open-source licenses as specified within the project directories.

## Contact

If you have any questions, concerns, or suggestions regarding this data collection initiative or the use of your projects, please contact us through the repository's issue tracker.

We appreciate your participation and contributions to improving the Language Model's code generation capabilities for Godot 4 projects. Together, we can enhance the development experience for the Godot community.
