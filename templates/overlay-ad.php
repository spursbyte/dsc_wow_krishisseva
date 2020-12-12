
<style>

  #overlay-ad .image{
    position:relative;
  }
#overlay-ad {
    position: fixed;
    text-align: center;
    top: 0;
  right:0;
    height: 100%;
    width: 100%;
    z-index: 9999;
    min-height: 500px;
}
  #overlay-ad .wrap {
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
    -webkit-align-items: center;
    align-items: center;
    -webkit-justify-content: center;
    justify-content: center;
    height: 100vh;
}
  #overlay-ad:before {
    content: '';
    position: fixed;
    width: 100%;
    height: 100%;
    left: 0;
    top: 0;
    background: rgba(0, 0, 0, 0.8);
}
  #overlay-ad .icon-close {
    color: #fff;
    cursor: pointer;
    float: right;
    height: 28px;
    width: 28px;
    border: 1px solid #fff;
    position: absolute;
    top: -8px;
    right: -10px;
    border-radius: 50%;
    line-height: 1.8;
    background: #ff0000;
    font-weight: bold;
    font-size: 0.9em;
}
.icon-close span{
    position: absolute;
    font-size: 0.8em;
    left: 6px;
}
</style>
<div id="overlay-ad" onclick="hideOverlay();">
   <div class="wrap">
      <div class="image">
         <span style="font-family: Arial; font-size:12px;display:block;text-align:left;color:#ccc">Advertisement</span>
         <div class="bg-lightgray  text-center ">
            <a target="_blank" href="http://letzcricket.com">
                <img src="img7.jpg" class="img-responsive">
            </a>
         </div>
         <i class="icon-close" onclick="hideOverlay();"><span>X</span></i>
      </div>
   </div>
</div>
<script>
  function hideOverlay(){
        document.getElementById('overlay-ad').style.display = 'none';
    }
  
</script>