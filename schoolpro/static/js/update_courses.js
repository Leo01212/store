document.addEventListener('DOMContentLoaded', function() {
    const departmentField = document.getElementById('id_department');
    const courseField = document.getElementById('id_course');

    const coursesMap = {
    'computer_science': [['bsc_computer_science', 'Bsc Computer Science'], ['bsc_computer_application', 'Bsc Computer Application']],
    'biology': [['bsc_botany', 'Bsc Botany'], ['bsc_zoology', 'Bsc Zoology']],
    'commerce': [['bba', 'BBA'], ['bcom', 'BCom']],
    'history': [['ba_history', 'BA History'], ['ba_politics', 'BA Politics']],
    'agriculture': [['bsc_agriculture', 'Bsc Agriculture'], ['msc_agriculture', 'Msc Agriculture']],
};

    departmentField.addEventListener('change', function() {
        const selectedDepartment = this.value;
        const courseOptions = coursesMap[selectedDepartment] || [];
        updateCourseOptions(courseOptions);
    });

    function updateCourseOptions(options) {
        // Clear existing options
        courseField.innerHTML = '';

        // Add new options
        options.forEach(([value, label]) => {
            const option = document.createElement('option');
            option.value = value;
            option.text = label;
            courseField.appendChild(option);
        });
    }

    // Initialize options on page load
    updateCourseOptions([]);
});

