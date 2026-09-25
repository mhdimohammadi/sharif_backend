var mybutton = document.getElementById('myBtn')
window.onscroll = function () {
  scrollFunction()
}
function scrollFunction () {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = 'block'
  } else {
    mybutton.style.display = 'none'
  }
}
function topFunction () {
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

// //  --------------------------back to top-------------------------------------

document.addEventListener('DOMContentLoaded', function () {
  var pageElement = document.querySelector('#home1,#home4,#about-us')
  if (pageElement) {
    animateCounter('customersCounter', 80)
    animateCounter('projectsCounter', 200)
    animateCounter('partnersCounter', 130)
    animateCounter('currentProjectsCounter', 90)
  }
})

function animateCounter (elementId, targetValue) {
  var currentValue = 0
  var counterElement = document.getElementById(elementId)

  var intervalId = setInterval(function () {
    if (currentValue < targetValue) {
      currentValue++
      counterElement.textContent = currentValue
    } else {
      clearInterval(intervalId)
    }
  }, 10)
}
// ---------------------------counter up-----------------------------------

var pages = ['home1', 'home2', 'home3', 'home4']

for (var i = 0; i < pages.length; i++) {
  var pageName = pages[i]
  var pageElement = document.querySelector('#' + pageName)
  if (pageElement) {
    var swiperElements = pageElement.querySelectorAll('.swiper-container')
    swiperElements.forEach(function (swiperElement) {
      var swiper = new Swiper(swiperElement, {
        spaceBetween: 10,
        autoplay: {
          delay: 5000
        },
        pagination: {
          el: '.swiper-pagination',
          clickable: true
        },
        breakpoints: {
          320: {
            slidesPerView: 1,
            spaceBetween: 20
          },
          640: {
            slidesPerView: 2,
            spaceBetween: 30
          },
          992: {
            slidesPerView: 3,
            spaceBetween: 30
          }
        }
      })
    })
  }
}

// -----------------------------swiper slider1 blog------------------------------
var pages = ['home2', 'home3']
for (var i = 0; i < pages.length; i++) {
  var pageName = pages[i]
  var pageElement = document.querySelector('#' + pageName)
  if (pageElement) {
    var swiperElements = pageElement.querySelectorAll('.swiper-container-2')
    swiperElements.forEach(function (swiperElement) {
      var swiper = new Swiper(swiperElement, {
        spaceBetween: 10,
        autoplay: {
          delay: 5000
        },
        pagination: {
          el: '.swiper-pagination-2',
          clickable: true
        },
        breakpoints: {
          320: {
            slidesPerView: 1,
            spaceBetween: 20
          },
          640: {
            slidesPerView: 2,
            spaceBetween: 30
          },
          992: {
            slidesPerView: 3,
            spaceBetween: 30
          }
        }
      })
    })
  }
}

//  ------------------------ swiper slider2 project----------------------------------

var pages = ['home4']

for (var i = 0; i < pages.length; i++) {
  var pageName = pages[i]
  var pageElement = document.querySelector('#' + pageName)
  if (pageElement) {
    var swiperElements = pageElement.querySelectorAll('.swiper-container-3')
    swiperElements.forEach(function (swiperElement) {
      var swiper = new Swiper(swiperElement, {
        spaceBetween: 10,
        autoplay: {
          delay: 5000
        },
        pagination: {
          el: '.swiper-pagination-3',
          clickable: true
        },
        breakpoints: {
          320: {
            slidesPerView: 1,
            spaceBetween: 20
          },
          640: {
            slidesPerView: 2,
            spaceBetween: 30
          },
          992: {
            slidesPerView: 2,
            spaceBetween: 30
          }
        }
      })
    })
  }
}
//  ----------------------- swiper slider3 comment--------------------------------
document.addEventListener('DOMContentLoaded', function () {
  var pageElement = document.querySelector('#questions')

  if (pageElement) {
    var acc = document.getElementsByClassName('accordion-1')
    var i

    for (i = 0; i < acc.length; i++) {
      acc[i].addEventListener('click', function () {
        this.classList.toggle('active-questions')

        var panel = this.nextElementSibling

        if (panel.style.maxHeight) {
          panel.style.maxHeight = null
        } else {
          panel.style.maxHeight = panel.scrollHeight + 'px'
        }
      })
    }
  }
})

// ---------------------------accordeon--------------------------------------

document.addEventListener('DOMContentLoaded', function () {
  var pageElement = document.querySelector('#product-detail')

  if (pageElement) {
    var increaseButton = document.getElementById('increase')
    var decreaseButton = document.getElementById('decrease')
    var counterElement = document.getElementById('counter')

    var counterValue = 0
    function increaseCounter () {
      counterValue++
      counterElement.innerText = counterValue
    }

    function decreaseCounter () {
      if (counterValue > 0) {
        counterValue--

        counterElement.innerText = counterValue
      }
    }

    increaseButton.addEventListener('click', increaseCounter)
    decreaseButton.addEventListener('click', decreaseCounter)
  }
})

// -------------------------product add----------------------------------

document.addEventListener('DOMContentLoaded', function () {
  var pageElement = document.querySelector('#basket')
  if (pageElement) {
    var increaseButtons = document.querySelectorAll('#increase')
    var decreaseButtons = document.querySelectorAll('#decrease')
    var counterElements = document.querySelectorAll('.counter')

    var counterValues = Array(counterElements.length).fill(0)

    function updateCounterDisplay (index) {
      counterElements[index].innerText = counterValues[index]
    }

    function increaseCounter (index) {
      counterValues[index]++
      updateCounterDisplay(index)
    }

    function decreaseCounter (index) {
      if (counterValues[index] > 0) {
        counterValues[index]--
        updateCounterDisplay(index)
      }
    }

    increaseButtons.forEach(function (button, index) {
      button.addEventListener('click', function () {
        increaseCounter(index)
      })
    })

    decreaseButtons.forEach(function (button, index) {
      button.addEventListener('click', function () {
        decreaseCounter(index)
      })
    })
  }
})

// -------------------------product add basket------------------------------------

document.addEventListener('DOMContentLoaded', function () {
  var pageElement = document.querySelector('#coming-soon')
  if (pageElement) {
    var days = 875

    var hours = 12

    var minutes = 50

    var seconds = 30

    var totalSeconds =
      days * 24 * 60 * 60 + hours * 60 * 60 + minutes * 60 + seconds

    var countdownInterval = setInterval(function () {
      var daysLeft = Math.floor(totalSeconds / (24 * 60 * 60))

      var hoursLeft = Math.floor((totalSeconds % (24 * 60 * 60)) / (60 * 60))

      var minutesLeft = Math.floor((totalSeconds % (60 * 60)) / 60)

      var secondsLeft = Math.floor(totalSeconds % 60)

      document.getElementById('days').getElementsByTagName('p')[0].textContent =
        daysLeft

      document
        .getElementById('hours')
        .getElementsByTagName('p')[0].textContent = hoursLeft

      document
        .getElementById('minutes')
        .getElementsByTagName('p')[0].textContent = minutesLeft

      document
        .getElementById('seconds')
        .getElementsByTagName('p')[0].textContent = secondsLeft

      totalSeconds--

      if (totalSeconds < 0) {
        clearInterval(countdownInterval)

        document.getElementById('countdown').textContent = 'زمان به پایان رسید!'
      }
    }, 1000)
  }
})

// --------------------------timer----------------------------------------
let dropdowns = document.querySelectorAll('.dropdown-toggle')
dropdowns.forEach(dd => {
  dd.addEventListener('click', function (e) {
    var el = this.nextElementSibling
    el.style.display = el.style.display === 'block' ? 'none' : 'block'
  })
})
// ------------------------dropdown---------------------------------------
var pages = ['product-detail']

for (var i = 0; i < pages.length; i++) {
  var pageName = pages[i]
  var pageElement = document.querySelector('#' + pageName)
  if (pageElement) {
    var swiperElements = pageElement.querySelectorAll('.swiper-product')
    swiperElements.forEach(function (swiperElement) {
      var swiper = new Swiper(swiperElement, {
        spaceBetween: 10,
        autoplay: {
          delay: 5000
        },
        loop: true,
        pagination: {
          el: '.swiper-pagination-4',
          clickable: true
        },
        breakpoints: {
          320: {
            slidesPerView: 1,
            spaceBetween: 20
          },
          640: {
            slidesPerView: 2,
            spaceBetween: 30
          },
          992: {
            slidesPerView: 3,
            spaceBetween: 30
          }
        }
      })
    })
  }
}

// --------------------------swiper slider product-----------------------------
