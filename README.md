# barbhost

A standalone HTML/JS tool that loads a Wix-style product CSV, displays each unit with name, price, and image, allows selecting items, and exports selected names to CSV. Designed to host on GitHub Pages and embed in a Wix iframe for customers to view but not edit.

## 🚀 Hosting on GitHub Pages

### Step 1: Push to GitHub
1. Create a new repository on GitHub (or use an existing one)
2. Push all files to your repository:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git push -u origin main
   ```

### Step 2: Enable GitHub Pages
1. Go to your repository on GitHub
2. Click **Settings** → **Pages**
3. Under **Source**, select **Deploy from a branch**
4. Choose **main** branch and **/ (root)** folder
5. Click **Save**
6. Your site will be available at: `https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/`

## 📱 Embedding in an Iframe

### For Wix Sites:
1. Add an **HTML iframe** element to your Wix page
2. Use this embed code (replace with your GitHub Pages URL):
   ```html
   <iframe 
       src="https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/index.html"
       width="100%"
       height="800"
       frameborder="0"
       title="Ready Units Collection"
       allowfullscreen>
   </iframe>
   ```

### For Other Websites:
See `iframe-example.html` for a complete example of how to embed the catalog.

## 📁 Files
- `index.html` - Main product catalog page
- `products.csv` - Product data (update this file to change products)
- `iframe-example.html` - Example page showing how to embed the catalog

## 🔧 Customization
- Update `products.csv` to add/modify products
- The catalog automatically loads and displays products from `products.csv`
- All styling is contained within `index.html`
