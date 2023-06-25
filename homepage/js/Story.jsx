import PropTypes from 'prop-types';
import React from 'react'

class Story extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      text: ""
    }
  }

  componentDidMount() {
    const { text } = this.props;

    this.setState({ text });
  }

  render() {
    const { keyNum } = this.props;
    const { text } = this.state;
    return (
      <div className='story'>
        <div className='story-content' key={keyNum}>
          <p>{text}</p>
        </div>
      </div>
    );
  }
}

Story.propTypes = {
  // prop types go here
  text: PropTypes.string.isRequired,
  keyNum: PropTypes.number.isRequired,
};

Story.defaultProps = {
  // default prop values go here if not required
};

export default Story
