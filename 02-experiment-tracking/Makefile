# Makefile for ML/Git Operations

# ==============================================================================
#  MLflow Target
# ==============================================================================

.PHONY: env

env:
	@conda activate exp-tracking-env


# 告诉 'make'， 'ui' 只是一个命令，而不是一个文件
.PHONY: ui

# 启动 MLflow UI
# 用法: make ui
ui:
	@echo "Starting MLflow UI (Backend: sqlite:///mlflow.db)..."
	@mlflow ui --backend-store-uri sqlite:///mlflow.db

# ==============================================================================
#  Git Targets
# ==============================================================================

# 告诉 'make'， 'push' 只是一个命令
.PHONY: push

# 快速添加、提交和推送代码
# 用法: make push m="你的提交信息"
push:
	@if [ -z "$(m)" ]; then \
		echo "ERROR: Commit message 'm' is required."; \
		echo "Usage: make push m=\"Your message\""; \
		exit 1; \
	fi
	@echo "--- 1. Adding all changes ---"
	@git add .
	@echo "--- 2. Committing with message: '$(m)' ---"
	@git commit -m "$(m)"
	@echo "--- 3. Pushing to remote repository ---"
	@git push