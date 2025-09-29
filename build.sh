#!/usr/bin/env bash
# build.sh
set -o errexit

echo "🔧 Installing Python packages..."
pip install -r requirements.txt

echo "📁 Setting up directories..."
mkdir -p staticfiles
mkdir -p media

echo "🎨 Collecting static files..."
python manage.py collectstatic --no-input --clear --verbosity=2
echo "✅ Static files collected to: $(pwd)/staticfiles"

echo "� Listing collected static files..."
find staticfiles -name "*.css" -o -name "*.js" | head -10

echo "�🗄️ Running database migrations..."
python manage.py migrate --verbosity=2

echo "🏁 Build completed successfully!"