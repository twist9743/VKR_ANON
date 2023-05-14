let file = document.getElementById("upload_file")
let btn = document.getElementById("btn_file")
window.onload = function () {
    file = document.getElementById("upload_file")
    btn = document.getElementById("btn_file")
}
btn.addEventListener("click", function () {
    let event = new MouseEvent("click", { bubbles: true })
    file.dispatchEvent(event)
})
file.addEventListener("change", async function (event) {
    let file = event.target.files[0]
    let formData = new FormData()
    formData.append("file", file)
    let req = await fetch("/api/upload_file", {
        method: "POST",
        body: formData
    })
    let res = await req.json();

    if (res.error == true) {
        console.log(res.message)
        return
    }

    window.location.href = "/results"
})


