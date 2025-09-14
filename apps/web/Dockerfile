FROM node:20-alpine
WORKDIR /app
COPY package.json package-lock.json* pnpm-lock.yaml* yarn.lock* ./
RUN npm set fund false && npm set audit false || true
# Install deps if lockfile present; ignore failure if none
RUN if [ -f package-lock.json ]; then npm ci; else npm install --package-lock=false; fi || true
COPY . .
EXPOSE 3000
CMD ["npm", "run", "dev"]

