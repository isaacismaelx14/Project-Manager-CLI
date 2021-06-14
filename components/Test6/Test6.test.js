import React from "react";
import "@testing-library/jest-dom";
import { render } from "@testing-library/react";
import Test6 from "./";
describe("<Test6 />", () => {
  let component;
  beforeEach(() => {
    component = render(<Test6 />);
  });
  test("should render", () => {
    component.getByText("Test6");
  });
});