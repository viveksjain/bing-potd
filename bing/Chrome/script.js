/* Store and display the image given by `img_url`. */
function store_img(fs, img_url) {
  var xhr = new XMLHttpRequest();
  xhr.open('GET', img_url, true);
  xhr.responseType = 'blob';

  xhr.onload = function(e) {
    if (this.status == 200) {
      var blob = this.response;

      fs.root.getFile('img.jpg', {create: true}, function(fileEntry) {
        fileEntry.createWriter(function(fileWriter) {
          fileWriter.onwriteend = function(e) {
            localStorage.cached_img_url = img_url;
            show_img(fs);
          };

          fileWriter.write(blob);
        });
      });
    }
  };

  xhr.send();
}

/* Show the currently cached image. */
function show_img(fs) {
  fs.root.getFile('img.jpg', {}, function(fileEntry) {
    $('body').css('background-image', 'url(' + fileEntry.toURL() + ')');
  });
}

/* Show the cached image, and if online then store and display the new one. */
function init_fs(fs) {
  show_img(fs);

  if (navigator.onLine) {
    $.get('http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1', function(data) {
      var img_url = 'http://www.bing.com' + data.images[0].url;
      if (localStorage.cached_img_url != img_url) {
        store_img(fs, img_url);
      }
    });
  }
}

window.webkitRequestFileSystem(window.PERSISTENT, 5*1024*1024, init_fs);
