###  Quick Start

Init the npm project. 
- Make sure to:
  - Set `main.js` as the entrypoint.
  - Add an author
  - Add an description
```sh
npm init
npm i -D electron@19.0.1
npm i -D @electron-forge/cli
npx electron-forge import
```

Ensure the `.gitignore` file.
```sh
echo "**/node_modules" >> .gitignore
echo "**/out" >> .gitignore
````



To run the development server.
```sh
npm start
```

To package the app.
```sh
npm run make
```

