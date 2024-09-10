document.addEventListener('DOMContentLoaded', function() {
    const passwordInput = document.getElementById('password');
    const confirmPasswordInput = document.getElementById('confirmPassword');
    const passwordStrengthDiv = document.getElementById('passwordStrength');

    function checkPasswordStrength(password) {
        let strength = 'Débil';
        const regex = {
            lower: /[a-z]/,
            upper: /[A-Z]/,
            digit: /\d/,
            special: /[!@#$%^&*(),.?":{}|<>]/
        };

        if (password.length >= 8 &&
            regex.lower.test(password) &&
            regex.upper.test(password) &&
            regex.digit.test(password) &&
            regex.special.test(password)) {
            strength = 'Fuerte';
        } else if (password.length >= 6 &&
            (regex.lower.test(password) || regex.upper.test(password)) &&
            (regex.digit.test(password) || regex.special.test(password))) {
            strength = 'Moderada';
        }

        return strength;
    }

    passwordInput.addEventListener('input', function() {
        const password = passwordInput.value;
        const strength = checkPasswordStrength(password);
        passwordStrengthDiv.textContent = `Fuerza de la contraseña: ${strength}`;
        passwordStrengthDiv.className = `password-strength ${strength.toLowerCase()}`;
    });

    confirmPasswordInput.addEventListener('input', function() {
        if (confirmPasswordInput.value !== passwordInput.value) {
            confirmPasswordInput.setCustomValidity('Las contraseñas no coinciden');
        } else {
            confirmPasswordInput.setCustomValidity('');
        }
    });
});

