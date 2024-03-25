function handleFileInputChange(inputId) {
  const input = document.getElementById(inputId);
  const container = document.getElementById('selected-images-container');
  

  for (let i = 0; i < input.files.length; i++) {
      const file = input.files[i];
      const reader = new FileReader();

      const imgWrapper = document.createElement('div');
      const img = document.createElement('img');
      const closeButton = document.createElement('button');

      imgWrapper.classList.add('mr-2', 'mb-2', 'relative');

      img.classList.add('w-60', 'h-40', 'rounded-lg');

      reader.onload = function(e) {
          img.src = e.target.result;
      };

      reader.readAsDataURL(file);

      closeButton.innerHTML = '<i class="fas fa-times rounded-full"></i>';
      closeButton.classList.add('absolute', 'w-10','h-10', 'hover:bg-gray-600', 'top-2', 'right-2', 'bg-gray-500', 'text-white', 'rounded-full', 'p-1', 'cursor-pointer', 'hidden');
      closeButton.addEventListener('click', function() {
          imgWrapper.remove(); 
      });

      imgWrapper.addEventListener('mouseover', function() {
          closeButton.classList.remove('hidden');
      });
      imgWrapper.addEventListener('mouseout', function() {
          closeButton.classList.add('hidden');
      });

      imgWrapper.appendChild(img);
      imgWrapper.appendChild(closeButton);

      container.appendChild(imgWrapper);
  }
}

function handleAttachmentInputChange() {
const input = document.getElementById('attachment-upload');
const container = document.getElementById('selected-attachments-container');

for (let i = 0; i < input.files.length; i++) {
    const file = input.files[i];
    const fileName = file.name;

    const attachmentWrapper = document.createElement('div');
    const fileIcon = document.createElement('i');
    const attachmentName = document.createElement('span');
    const closeButton = document.createElement('button');

    attachmentWrapper.classList.add('mr-2', 'mb-2', 'relative');

    fileIcon.classList.add('fas', 'fa-file', 'text-gray-400', 'mr-1');

    attachmentName.textContent = fileName;

    closeButton.innerHTML = 'Remove';
    closeButton.classList.add('text-white', 'rounded-md', 'ml-2', 'bg-red-500', 'hover:bg-red-600', 'p-2', 'cursor-pointer');
    closeButton.addEventListener('click', function() {
        attachmentWrapper.remove(); 
    });

    attachmentWrapper.appendChild(fileIcon);
    attachmentWrapper.appendChild(attachmentName);
    attachmentWrapper.appendChild(closeButton);

    container.appendChild(attachmentWrapper);
}
}


document.getElementById('picture-upload').addEventListener('change', function() {
  handleFileInputChange('picture-upload');
});
document.getElementById('attachment-upload').addEventListener('change', handleAttachmentInputChange);
