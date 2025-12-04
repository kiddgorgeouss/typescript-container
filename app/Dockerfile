# syntax=docker/dockerfile:1

# Use Node.js 18 LTS (Long Term Support) for better compatibility
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Set environment variables
ENV NODE_ENV=development

# Copy package files
COPY package*.json ./

# Copy application files
COPY . .

# Expose the application port
EXPOSE 8000

# Start the development server
CMD ["npm", "start"]
