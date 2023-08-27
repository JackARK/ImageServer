const express = require('express');
const multer = require('multer');
const fs = require('fs-extra');
const path = require('path');
const morgan = require('morgan');

const app = express();
const upload = multer();

// 创建日志文件
const accessLogStream = fs.createWriteStream(path.join(__dirname, 'access.log'), { flags: 'a' });

// 使用 morgan 中间件记录日志
app.use(morgan('combined', { stream: accessLogStream }));

app.use(express.static('uploads'));

app.post('/upload/:folder', upload.single('image'), (req, res) => {
  if (!req.file) {
    return res.status(400).json({ error: 'No file uploaded' });
  }
  console.log(req.file)
  const folder = req.params.folder;
  const folderPath = path.join(__dirname, 'uploads', folder);
  const imagePath = path.join(folderPath, req.file.originalname);

  fs.ensureDir(folderPath)
    .then(async () => {
      // return await fs.move(req.file.path, imagePath, { overwrite: true }); 
      return await fs.writeFile(path.join(__dirname + "/uploads/" + req.params.folder, req.file.originalname), req.file.buffer)

    })
    .then(() => {
      console.log(`Image uploaded to ${imagePath}`);
      res.json({ success: true });
    })
    .catch((err) => {
      console.error(err);
      res.status(500).json({ error: 'Error uploading file' });
    });
});

app.get('/random/:folder', (req, res) => {
  const folder = req.params.folder;
  const folderPath = path.join(__dirname, 'uploads', folder);

  fs.readdir(folderPath, (err, files) => {
    if (err) {
      console.error(err);
      return res.status(500).json({ error: 'Error retrieving images' });
    }

    const randomIndex = Math.floor(Math.random() * files.length);
    const imagePath = path.join(folderPath, files[randomIndex]);

    res.sendFile(imagePath);
    console.log(`An image has been sent: ${imagePath}`);
  });
});

const port = 4399;
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
