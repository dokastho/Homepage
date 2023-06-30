import PropTypes from 'prop-types';
import React from 'react'
import { SmallIconWithText } from './smallIcon';

class Picker extends React.Component {

  constructor(props) {
    super(props);
    this.setTopicFocusWrapper = this.setTopicFocusWrapper.bind(this);
  }

  setTopicFocusWrapper(args) {
    const { idx } = args;
    const { setTopicFocus } = this.props;
    setTopicFocus(idx);
  }

  render() {
    const {
      topics,
    } = this.props;
    return (
      <div className='picker'>
        {
          topics.map((topic) => {
            const { idx, name, icon } = topic;
            return <SmallIconWithText src={`/static/img/${icon}`} text={name} keyName={`${idx}`} onClick={this.setTopicFocusWrapper} args={{ idx }} />
          })
        }
      </div>
    );
  }
}

Picker.propTypes = {
  topics: PropTypes.instanceOf(Array).isRequired  // array of pairs: name and topicId

  // methods
  // setTopicFocus
};

Picker.defaultProps = {
  // default prop values go here if not required
};

export default Picker
