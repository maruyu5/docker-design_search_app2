// 検索ボタンを押したときのアニメーション
$(function () {
	const searchForm = $(".search-form");
	const searchBtn = $(".search-btn");
	searchBtn.on("click", function(e) {
		e.preventDefault();
        $("#loader-wrap").show();
        $("#loader-wrap").delay(200).fadeOut();
        setTimeout(function(){
            searchForm.submit();
        }, 450 );
    });
});

// ツールチップの有効化（Bootstrap）
window.onload = function() {
    const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
    const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))
}