$(".chosen-select").each(function () {
    $(this).chosen({});
});

let el_id = 1;

$('#add_element').on('click', function(){
    html = `
    <div class="element">
        <div class="form">
            <input type="hidden" name="el_id_${el_id}" value="${el_id}" id="el_id_${el_id}">
            <div class="inputrow">
                <div class="inputgroup">
                    <label for="el_name">Вопрос</label>
                    <input type="text" name="el_name_${el_id}" id="el_name_${el_id}">
                </div>
                <div class="inputgroup">
                    <label for="el_name">Тип</label>
                    <select name="el_type_${el_id}" id="el_type_${el_id}" class="chosen-select" onchange="changeElement(event)">
                        <option value="one_in_list">Один из списка</option>
                        <option value="many_in_list">Неколько из списка</option>
                        <option value="string">Строка</option>
                        <option value="textarea" selected>Текст с абзацами</option>
                        <option value="range">Шкала</option>
                    </select>
                </div>
            </div>
            <div class="variants"></div>
            <div class="inputgroup">
                <input type="file" name="el_file_${el_id}">
                <input type="checkbox" class="checkbox" name="el_required_${el_id}" value="1" id="el_required_${el_id}">
                <label for="el_required_${el_id}">Обязательное поле</label>
            </div>
        </div>
    </div>
    `
    $('.elements').append(html);
    $(`#el_type_${el_id}`).chosen({});

    el_id += 1;
})

function set_one_in_list_element(id, element, name) {
    html = `
        <label for="el_text_${id}">Варианты ответов</label>
        <input type="hidden" data-id="textarea" name="el_text_${id}">
        <div class="radio__type__variant">
            <i class="icon-circle variant__icon"></i>
            <input type="text" name="variant_text" placeholder="Ваш вариант">
            <i class="icon-x variant__icon variant__delete"></i>
        </div>
        <div class="btn add_variant radios"><i class="icon-plus"></i> Добавить вариант</div>
    `;

    $(`#el_id_${id}`).val(id);
    $(element).find('.variants').html(html);
}

function set_many_in_list_element(id, element, name) {
    html = `
        <label for="el_text_${id}">Варианты ответов</label>
        <input type="hidden" data-id="textarea" name="el_text_${id}">
        <div class="check__type__variant">
            <i class="icon-square variant__icon"></i>
            <input type="text" name="variant_text" placeholder="Ваш вариант">
            <i class="icon-x variant__icon variant__delete"></i>
        </div>
        <div class="btn add_variant checks"><i class="icon-plus"></i> Добавить вариант</div>
    `
    $(`#el_id_${id}`).val(id);
    $(element).find('.variants').html(html);
}
function set_string_element(id, element, name) {
    html = ``;
    $(`#el_id_${id}`).val(id);
    $(element).find('.variants').html(html);
}
function set_textarea_element(id, element, name) {
    html = ``;
    $(`#el_id_${id}`).val(id);
    $(element).find('.variants').html(html);
}
function set_range_element(id, element, name) {
    html = `
        <div class="inputrow">
            <div class="inputgroup">
                <label>Минимальное</label>
                <select name="el_range_min_${id}" class="chosen-select" id="el_range_min_${id}">
                    <option value="0" selected>0</option>
                    <option value="1">1</option>
                </select>
            </div>    
            <div class="inputgroup">
                <label>Максимальное</label>
                <select name="el_range_max_${id}" class="chosen-select" id="el_range_max_${id}">
                    <option value="2" selected>2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                    <option value="5">5</option>
                    <option value="6">6</option>
                    <option value="7">7</option>
                    <option value="8">8</option>
                    <option value="9">9</option>
                    <option value="10">10</option>
                </select>
            </div>
        </div>
    `
    $(`#el_id_${id}`).val(id);
    $(element).find('.variants').html(html);

    $(`#el_range_min_${id}`).chosen({});
    $(`#el_range_max_${id}`).chosen({});
}

function addRadioVariantElement() {
    html = `<div class="radio__type__variant">
                <i class="icon-circle variant__icon"></i>
                <input type="text" name="variant_text" placeholder="Ваш вариант">
                <i class="icon-x variant__icon variant__delete"></i>
            </div>`
    return html;
}

function addCheckVariantElement() {
    html = `<div class="check__type__variant">
                <i class="icon-square variant__icon"></i>
                <input type="text" name="variant_text" placeholder="Ваш вариант">
                <i class="icon-x variant__icon variant__delete"></i>
            </div>`
    return html;
}

function changeElement(e) {
    
    let target = $(e.target)
    let selected_type = target.val()
    let element_block = target.parent().parent().parent();
    let element_id = element_block.find(':input').val()
    let element_name = element_block.find(`:input[name=el_name_${element_id}]`).val()
    if (selected_type == 'one_in_list') {
        set_one_in_list_element(element_id, element_block, element_name)
    }
    if (selected_type == 'many_in_list') {
        set_many_in_list_element(element_id, element_block, element_name)
    }
    if (selected_type == 'string') {
        set_string_element(element_id, element_block, element_name)
    }
    if (selected_type == 'textarea') {
        set_textarea_element(element_id, element_block, element_name)
    }
    if (selected_type == 'range') {
        set_range_element(element_id, element_block, element_name)
    }
    $('.elements').find('.add_variant.radios').on('click', function(){
        $(this).before(addRadioVariantElement());
        $('.variant__delete').on('click', function(){
            $(this).parent().remove();
        })
    })
    $('.elements').find('.add_variant.checks').on('click', function(){
        $(this).before(addCheckVariantElement());
        $('.variant__delete').on('click', function(){
            $(this).parent().remove();
        })
    })

}

$('form').on('submit', function(){
    $('.element').each(function(i) {
         if ($(this).find('.radio__type__variant').length > 0) {
             var text_el = $(this).find('input[type="hidden"]')[1]
             var arr = [];
             $(this).find('.variants .radio__type__variant').each(function(j) {
                 var val = $(this).find('input[name="variant_text"]').val()
                 arr.push(val)
             })
             $(text_el).val(arr.join('\n'))
         }
         if ($(this).find('.check__type__variant').length > 0) {
            var text_el = $(this).find('input[type="hidden"]')[1]
            var arr = [];
            $(this).find('.variants .check__type__variant').each(function(j) {
                var val = $(this).find('input[name="variant_text"]').val()
                arr.push(val)
            })
            $(text_el).val(arr.join('\n'))
        }
    })
})