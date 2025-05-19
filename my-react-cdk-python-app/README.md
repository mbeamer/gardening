# my-react-cdk-python-app/README.md

# My React CDK Python App

This project is an AWS CDK application that deploys a React app to an S3 bucket and configures Route 53 for the domain thebeamers.ca.

## Project Structure

- `app.py`: Entry point of the CDK application.
- `cdk.json`: Configuration settings for the CDK application.
- `requirements.txt`: Python dependencies required for the project.
- `src/my_react_cdk_python_app/`: Contains the CDK stack and configuration.
- `react_app/`: Contains the React application source code and assets.
- `tests/`: Contains unit tests for the CDK stack.

## Setup Instructions

1. **Install AWS CDK**: Make sure you have the AWS CDK installed. You can install it globally using npm:

   ```
   npm install -g aws-cdk
   ```

2. **Install Python Dependencies**: Navigate to the project directory and install the required Python packages:

   ```
   pip install -r requirements.txt
   ```

3. **Deploy the Stack**: To deploy the CDK stack, run the following command:

   ```
   cdk deploy
   ```

4. **Access the React App**: Once the deployment is complete, you can access your React app at the configured domain thebeamers.ca.

## Usage

You can modify the stack in `src/my_react_cdk_python_app/stack.py` to customize the resources created by the CDK application. Make sure to update the configuration in `src/my_react_cdk_python_app/config.py` as needed.

## Running Tests

To run the unit tests for the CDK stack, use the following command:

```
pytest tests/test_stack.py
```