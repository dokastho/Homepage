import PropTypes from 'prop-types';
import React from 'react'

class Topic extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    const {
      content,
      setTopicFocus,
      topicIdx,
      maxTopicIdx,
    } = this.props;

    const topicName = content?.name;

    return (
      <div className='topic'>
        <h1>{topicName}</h1>
        {
          topicIdx === 0 ? null : (
            <button onClick={() => { setTopicFocus(topicIdx - 1) }}>&lt;-</button>
          )
        }
        {
          topicIdx === maxTopicIdx ? null : (
            <button onClick={() => { setTopicFocus(topicIdx + 1) }}>-&gt;</button>
          )
        }
      </div>
    );
  }
}

Topic.propTypes = {
  // prop types go here
  content: PropTypes.object.isRequired,
  topicIdx: PropTypes.number.isRequired,
  maxTopicIdx: PropTypes.number.isRequired,

  // methods:
  // setTopicFocus
};

Topic.defaultProps = {
  // default prop values go here if not required
};

export default Topic

