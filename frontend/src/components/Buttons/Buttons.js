import React from 'react'

//css
import './Buttons.css'


//Filled Button
const PrimaryButton = ({ showLeftIcon, leftIcon, showbuttonText, buttonText, showRightIcon, rightIcon, onClick }) => {
  return (
    <button className='primary-btn' onClick={onClick}>
        {showLeftIcon && <img src={leftIcon} alt='icon' className='icon-32px' />}
        {showbuttonText && <div className='button-text'>{buttonText}</div>}
        {showRightIcon && <img src={rightIcon} alt='icon' className='icon-32px' />}
    </button>
  )
}

//Filled Tonal-Grey 
const SecondaryButton = ({ showLeftIcon, leftIcon, showbuttonText, buttonText, showRightIcon, rightIcon, onClick }) => {
    return (
      <button className='primary-btn' onClick={onClick}>
          {showLeftIcon && <img src={leftIcon} alt='icon' className='icon-32px' />}
          {showbuttonText && <div className='button-text'>{buttonText}</div>}
          {showRightIcon && <img src={rightIcon} alt='icon' className='icon-32px' />}
      </button>
    )
  }

const OutlineButton = ({ showLeftIcon, leftIcon, showbuttonText, buttonText, showRightIcon, rightIcon, onClick }) => {
return (
    <button className='primary-btn' onClick={onClick}>
        {showLeftIcon && <img src={leftIcon} alt='icon' className='icon-32px' />}
        {showbuttonText && <div className='button-text'>{buttonText}</div>}
        {showRightIcon && <img src={rightIcon} alt='icon' className='icon-32px' />}
    </button>
)
}

const ElevatedButton = ({ showLeftIcon, leftIcon, showbuttonText, buttonText, showRightIcon, rightIcon, onClick }) => {
    return (
      <button className='primary-btn' onClick={onClick}>
          {showLeftIcon && <img src={leftIcon} alt='icon' className='icon-32px' />}
          {showbuttonText && <div className='button-text'>{buttonText}</div>}
          {showRightIcon && <img src={rightIcon} alt='icon' className='icon-32px' />}
      </button>
    )
  }

//Looks Like a Link 
const TertiaryButton = ({ showLeftIcon, leftIcon, showbuttonText, buttonText, showRightIcon, rightIcon, onClick }) => {
return (
    <button className='primary-btn' onClick={onClick}>
        {showLeftIcon && <img src={leftIcon} alt='icon' className='icon-32px' />}
        {showbuttonText && <div className='button-text'>{buttonText}</div>}
        {showRightIcon && <img src={rightIcon} alt='icon' className='icon-32px' />}
    </button>
)
}



export { PrimaryButton, SecondaryButton, OutlineButton, ElevatedButton, TertiaryButton }
