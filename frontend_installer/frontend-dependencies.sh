# Install sass compiler and node dependencies
brew install sass/sass/sass
brew install node@18
brew link node@18

# Install rtlcss globally
npm install -g rtlcss

# Install less globally
npm install -g less less-plugin-clean-css

# Verify installations
sass --version
node --version
npm --version
rtlcss --version
lessc --version

# Install additional web dependencies
npm install -g postcss-cli autoprefixer

# Create symlink for sassc
sudo ln -s /opt/homebrew/bin/sass /usr/local/bin/sassc

# Set permissions
sudo chown -R $USER /usr/local/lib/node_modules
sudo chown -R $USER /usr/local/bin
sudo chown -R $USER /usr/local/share
