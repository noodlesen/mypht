





$.ajaxSetup({
    beforeSend: function(xhr, settings) {
		var csrftoken = $('[name=csrfmiddlewaretoken]').attr('value');
        if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken)
		}
		
		
    }
})

function getResults(route, resultType, formData, callback){
	$.ajax(route,{
		type: 'post',
		data: JSON.stringify(formData, null, '\t'),
		dataType: resultType,
		contentType: 'application/json;charset=UTF-8',
		success: function(result){
			callback(result);
		},
		error: function(result){
			console.log(result);
			alert('Something went wrong :( \nTry to reload this page (F5 or Ctrl+R)');
			//location.reload();
		}
	});
}