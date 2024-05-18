chrome.runtime.onInstalled.addListener(() => {
  chrome.contextMenus.create({
    id: "downloadVideo",
    title: "Download YouTube Video (Highest Quality)",
    contexts: ["link"]
  });

  chrome.contextMenus.create({
    id: "downloadAudio",
    title: "Download YouTube Audio (Highest Quality)",
    contexts: ["link"]
  });
});

chrome.contextMenus.onClicked.addListener((info, tab) => {
  if (info.menuItemId === "downloadVideo") {
    fetch(`http://localhost:5000/download?url=${info.linkUrl}&type=video`)
      .then(response => response.text())
      .then(data => alert("Download started"))
      .catch(error => console.error('Error:', error));
  } else if (info.menuItemId === "downloadAudio") {
    fetch(`http://localhost:5000/download?url=${info.linkUrl}&type=audio`)
      .then(response => response.text())
      .then(data => alert("Download started"))
      .catch(error => console.error('Error:', error));
  }
});
