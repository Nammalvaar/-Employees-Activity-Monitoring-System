<div class="form-group m-2">
                <label for="empl_id">Employee Register ID</label>
                <input type="text" id="empl_id" name="empl_id" class="form-control mt-1" >
            </div>
<div class="col-lg-6 mt-3 text-center">
  <label  for="">Profile Image</label> 
  <div class="row">
    <div class="col-lg-12 emp-img d-flex justify-content-center">
                    <img src="../assets/image/9.png" class="img-fluid" alt="" id="capturedImage">
                </div>
                <div class="col-lg-12 emp-img d-flex justify-content-center">
                    <div class="form-group">
                        <button type="button" class="form-control bg-danger text-white m-2" id="captureBtn">Capture</button>
                        <button type="button" class="form-control bg-primary text-white m-2" id="retakeBtn" style="display: none">Retake</button>
                        <p id="alertMessage" class="alert alert-danger" style="display: none;">Please capture both document images before submitting.</p>
                      </div>
                </div>
            </div>
        </div>
<script>
    document.getElementById("captureBtn").addEventListener("click", function() {
        var empl_id = document.getElementById("empl_id").value;
        var duration = 10;

        var imageElement = document.getElementById("capturedImage");
        var retakeButton = document.getElementById("retakeBtn");
        var captureButton = document.getElementById("captureBtn");

        var xhr = new XMLHttpRequest();

        xhr.open("POST", "capture.php", true);
        xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

        xhr.onload = function() {
            if (xhr.status === 200) {
                var modal = new bootstrap.Modal(document.getElementById('addemployee'));
                imageElement.src = "../uploads/" + empl_id + "/frame_0000.jpg";
                retakeButton.style.display = "block";
                captureButton.style.display = "none";
                modal.show();
            }
        };
        xhr.send("capture=1&empl_id=" + empl_id + "&duration=" + duration);
    });

    document.getElementById("retakeBtn").addEventListener("click", function() {
        var imageElement = document.getElementById("capturedImage");
        var retakeButton = document.getElementById("retakeBtn");
        var captureButton = document.getElementById("captureBtn");
        
        imageElement.src = "";
        retakeButton.style.display = "none";
        captureButton.style.display = "block";
    });
</script>
