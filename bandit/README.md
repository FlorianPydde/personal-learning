# Bandit to check python code vulnerabilities

Bandit is a tool designed to find common security issues in Python code. To do this, Bandit processes each file, builds an AST from it, and runs appropriate plugins against the AST nodes. Once Bandit has finished scanning all the files, it generates a report.

## Learning Resources

To dive into the world of bandit and enhance your knowledge, I recommend exploring the following resources:

1. **[Official Pre-Commit Framework Documentation](https://bandit.readthedocs.io/en/latest/start.html)**: The official documentation provides a comprehensive guide on setting up and configuring pre-commits using the Pre-Commit framework.

2. **[Walkthrough](https://stackabuse.com/checking-vulnerabilities-in-your-python-code-with-bandit/)**: some useful stuff from stackOverflow.

## Requirements

1. First install pre-commit: ```pip install bandit```
2. Create default config file ```bandit-config-generator -o bandit.yaml```
3. run it: ```bandit -c bandit.yaml -r .``` or ```bandit -c bandit.yaml -r . -f csv -o out.csv```
