#!/usr/bin/env bash
# build.sh
set -o errexit

echo "🔧 Installing Python packages..."
pip install -r requirements.txt

echo "📁 Creating staticfiles directory..."
mkdir -p staticfiles

echo "🎨 Collecting static files..."
python manage.py collectstatic --no-input --clear --verbosity=2

echo "🗄️ Running database migrations..."
python manage.py migrate --verbosity=2

echo "✅ Build completed successfully!"
echo "📊 Static files location: $(pwd)/staticfiles"
ls -la staticfiles/ || echo "❌ Static files directory not found"