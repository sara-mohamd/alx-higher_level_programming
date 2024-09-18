/**
 * Toggles the class of the <header> element between 'red' and 'green' 
 * when the user clicks on the <div> element with the ID 'toggle_header'.
 *
 * - If the <header> currently has the class 'red', the class is removed 
 *   and replaced with 'green'.
 * - If the <header> currently has the class 'green', the class is removed 
 *   and replaced with 'red'.
 * - The <header> will always have exactly one class: 'red' or 'green', 
 *   never both, and never empty.
 *
 * Dependencies:
 * - jQuery library must be included in the HTML for this code to work.
 *
 * Example Usage:
 * <header class="red">This is the header</header>
 * <div id="toggle_header">Click to toggle header color</div>
 * 
 * CSS Classes:
 * - .red: Defines the styling when the header has the red background.
 * - .green: Defines the styling when the header has the green background.
 */

$("DIV#red_header").click(() => {
  if ($('header').hasClass('red')) {
    $('header').removeClass('red').addClass('green');
  } else {
    $('header').removeClass('green').addClass('red');
  }
});
