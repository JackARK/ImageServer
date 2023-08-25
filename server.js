const express = require('express');
const multer = require('multer');
const fs = require('fs-extra');
const path = require('path');

const app = express();
const upload = multer({ dest: 'uploads/' });

app.use(express.static('uploads'));

app.post('/upload', upload.single('image'), (req, res) => {
  if (!req.file) {
    return res.status(400).json({ error: 'No file uploaded' });
  }

  const imagePath = path.join(__dirname, req.file.path);
  const targetPath = path.join(__dirname, 'uploads', req.file.originalname);

  fs.move(imagePath, targetPath, { overwrite: true }, (err) => {
    if (err) {
      console.error(err);
      return res.status(500).json({ error: 'Error uploading file' });
    }
    console.log("A image accepted"+targetPath)
    res.json({ success: true });
  });
});

app.get('/random', (req, res) => {
  fs.readdir('uploads', (err, files) => {
    if (err) {
      console.error(err);
      return res.status(500).json({ error: 'Error retrieving images' });
    }

    const randomIndex = Math.floor(Math.random() * files.length);
    const imagePath = path.join(__dirname, 'uploads', files[randomIndex]);

    res.sendFile(imagePath);
    console.log('A image has been sent:'+imagePath)
  });
});

const port = 4399;
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
