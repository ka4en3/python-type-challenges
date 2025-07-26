FROM python:3.12-slim

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copy project files
COPY pyproject.toml .
COPY src/ src/

# Install dependencies
RUN uv venv && \
    . .venv/bin/activate && \
    uv pip install -e ".[dev]"

# Make venv available in PATH
ENV PATH="/app/.venv/bin:$PATH"

CMD ["bash"]