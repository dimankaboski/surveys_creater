let el_id = 1;

$('#add_element').on('click', function(){
    html = `
    <div class="element">
        <input type="hidden" name="el_id_${el_id}" value="${el_id}">
        <label for="el_name">Вопрос</label>
        <input type="text" name="el_name_${el_id}" id="el_name_${el_id}">
        <select name="el_type" class="el_type_${el_id}" id="" onchange="changeElement(event)">
            <option value="one_in_list">Один из списка</option>
            <option value="many_in_list">Неколько из списка</option>
            <option value="string">Строка</option>
            <option value="textarea" selected>Текст с абзацами</option>
            <option value="range">Шкала</option>
        </select>
        <textarea name="el_text_${el_id}" id="" cols="70" rows="5"></textarea>
    </div>
    `
    $('.elements').append(html);
    el_id += 1;
})

function set_one_in_list_element(id, element, name) {
    html = `
        <div class="element">
            <input type="hidden" name="el_id_${id}" value="${id}">
            <label for="el_name">Вопрос</label>
            <input type="text" name="el_name_${id}" id="el_name_${id}" value="${name}">
            <select name="el_type" class="el_type_${id}" id="" onchange="changeElement(event)">
                <option value="one_in_list" selected>Один из списка</option>
                <option value="many_in_list">Неколько из списка</option>
                <option value="string">Строка</option>
                <option value="textarea">Текст с абзацами</option>
                <option value="range">Шкала</option>
            </select>
            <textarea name="el_text_${id}" id="" cols="70" rows="5"></textarea>
        </div>
    `
    $(element).html(html);
}

function set_many_in_list_element(id, element, name) {
    html = `
        <div class="element">
            <input type="hidden" name="el_id_${id}" value="${id}">
            <label for="el_name">Вопрос</label>
            <input type="text" name="el_name_${id}" id="el_name_${id}" value="${name}">
            <select name="el_type" class="el_type_${id}" id="" onchange="changeElement(event)">
                <option value="one_in_list">Один из списка</option>
                <option value="many_in_list" selected>Неколько из списка</option>
                <option value="string">Строка</option>
                <option value="textarea">Текст с абзацами</option>
                <option value="range">Шкала</option>
            </select>
            <textarea name="el_text_${id}" id="" cols="70" rows="5"></textarea>
        </div>
    `
    $(element).html(html);
}
function set_string_element(id, element, name) {
    html = `
        <div class="element">
            <input type="hidden" name="el_id_${id}" value="${id}">
            <label for="el_name">Вопрос</label>
            <input type="text" name="el_name_${id}" id="el_name_${id}" value="${name}">
            <select name="el_type" class="el_type_${id}" id="" onchange="changeElement(event)">
                <option value="one_in_list">Один из списка</option>
                <option value="many_in_list">Неколько из списка</option>
                <option value="string" selected>Строка</option>
                <option value="textarea">Текст с абзацами</option>
                <option value="range">Шкала</option>
            </select>
            <input type="text" name="el_text_${id}" id="">
        </div>
    `
    $(element).html(html);
}
function set_textarea_element(id, element, name) {
    html = `
        <div class="element">
            <input type="hidden" name="el_id_${id}" value="${id}">
            <label for="el_name">Вопрос</label>
            <input type="text" name="el_name_${id}" id="el_name_${id}" value="${name}">
            <select name="el_type" class="el_type_${id}" id="" onchange="changeElement(event)">
                <option value="one_in_list">Один из списка</option>
                <option value="many_in_list" selected>Неколько из списка</option>
                <option value="string">Строка</option>
                <option value="textarea" selected>Текст с абзацами</option>
                <option value="range">Шкала</option>
            </select>
            <textarea name="el_text_${id}" id="" cols="70" rows="5"></textarea>
        </div>
    `
    $(element).html(html);
}
function set_range_element(id, element, name) {
    html = `
        <div class="element">
            <input type="hidden" name="el_id_${id}" value="${id}">
            <label for="el_name">Вопрос</label>
            <input type="text" name="el_name_${id}" id="el_name_${id}" value="${name}">
            <select name="el_type" class="el_type_${id}" id="" onchange="changeElement(event)">
                <option value="one_in_list">Один из списка</option>
                <option value="many_in_list" selected>Неколько из списка</option>
                <option value="string">Строка</option>
                <option value="textarea">Текст с абзацами</option>
                <option value="range" selected>Шкала</option>
            </select>
            <input type="number" value="1" min="1" max="1">
            <input type="number" value="2" min="2" max="10">
        </div>
    `
    $(element).html(html);
}

function changeElement(e) {
    
    let target = $(e.target)
    let selected_type = target.val()
    let element_block = target.parent()
    let element_id = element_block.find(':input').val()
    let element_name = element_block.find(`:input[name=el_name_${element_id}]`).val()
    if (selected_type == 'one_in_list') {
        set_one_in_list_element(el_id, element_block, element_name)
    }
    if (selected_type == 'many_in_list') {
        set_many_in_list_element(el_id, element_block, element_name)
    }
    if (selected_type == 'string') {
        set_string_element(el_id, element_block, element_name)
    }
    if (selected_type == 'textarea') {
        set_textarea_element(el_id, element_block, element_name)
    }
    if (selected_type == 'range') {
        set_range_element(el_id, element_block, element_name)
    }
}