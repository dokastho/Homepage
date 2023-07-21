import React from 'react';
import PropTypes from 'prop-types';

class SmallIconWithText extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      hovering: false,
    }
    this.handleMouseEnter = this.handleMouseEnter.bind(this);
    this.handleMouseLeave = this.handleMouseLeave.bind(this);
  }

  handleMouseEnter() {
    this.setState({ hovering: true });
  }
  handleMouseLeave() {
    this.setState({ hovering: false });
  }

  render() {
    const { src, text, onClick, keyName, args } = this.props;
    const { hovering } = this.state;
    return (
      <div className='small-icon-with-text'
        onMouseEnter={this.handleMouseEnter}
        onMouseLeave={this.handleMouseLeave}
        onClick={() => { onClick(args) }}
      >
        <object data={src} key={keyName} className='small-icon-img' />
        {
          <div className='small-icon-label'>
            {
              hovering ? <h5>{text}</h5> : null
            }
          </div>
        }
      </div>
    )
  }
}

SmallIconWithText.propTypes = {
  src: PropTypes.string.isRequired,
  text: PropTypes.string.isRequired,
  keyName: PropTypes.string.isRequired,
  args: PropTypes.instanceOf(Object).isRequired,
  // onClick: action method on click
};

class SmallTextIcon extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    const { text, className, onClick, args } = this.props;
    return (
      <h2 className={className} id='small-text' onClick={() => { onClick(args) }}>{text}</h2>
    )
  }
}

SmallTextIcon.propTypes = {
  text: PropTypes.string.isRequired,
  className: PropTypes.string.isRequired,
  args: PropTypes.instanceOf(Object),
  // onClick: action method on click
};

class SmallConfirmatoryTextIcon extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      selected: false
    }
    this.toggleSelect = this.toggleSelect.bind(this);
  }

  toggleSelect() {
    const { selected } = this.state;
    this.setState({ selected: !selected });
  }

  render() {
    const { selected } = this.state;
    const { text, className, onClick, args } = this.props;
    return (
      selected ? <h2 className={className} id='small-text-selected' onClick={() => { onClick(args) }}>{text}</h2> : <h2 className={className} id='small-text' onClick={() => { this.toggleSelect() }}>{text}</h2>
    )
  }
}

SmallConfirmatoryTextIcon.propTypes = {
  text: PropTypes.string.isRequired,
  className: PropTypes.string.isRequired,
  args: PropTypes.instanceOf(Object),
  // onClick: action method on click
};

export { SmallIconWithText, SmallTextIcon, SmallConfirmatoryTextIcon }
