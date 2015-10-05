var searchProduct = (function() {
	function UpdateResult() {
	}
	function getProducts {
	$.ajax( {
		url: 'products/search_product/',
		data: { name : $('#id_name').val() },
		type: 'GET',
		} );
	}
	function init() {
	$('#id_name').on('input', getProducts);
	}
	return {
	'init' : init 
	};
})();
$document.ready(searchProduct.init);
